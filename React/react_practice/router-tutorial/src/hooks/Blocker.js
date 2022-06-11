import { useContext, useEffect, useCallback } from "react";
import { UNSAFE_NavigationContext as NavigationContext } from "react-router-dom";

// history.block의 경우 로직을 이제 직접 구현해야 함.

export function useBlocker(blocker, when = true) {
    const { navigator } = useContext(NavigationContext);

    useEffect(() => {
        if (!when) return;

        const unblock = navigator.block((tx) => {
            const autoUnblockingTx = {
                ...tx,
                retry() {
                    unblock();
                    tx.retry();
                },
            };
            blocker(autoUnblockingTx);
        });
        return unblock;
    }, [navigator, blocker, when]);
}

export function usePrompt(message, when = true) {
    const blocker = useCallback(
        (tx) => {
            if (window.confirm(message)) tx.retry();
        },
        [message],
    );

    useBlocker(blocker, when);
}
