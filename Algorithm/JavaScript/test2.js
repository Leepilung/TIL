function solution(fetchExperts, fetchIsExpertOnline) {
    // 보험 전문가의 목록을 반환하는 비동기 함수 (반환 타입: Promise<string[]>)
    fetchExperts();
    
    // 보험 전문가가 온라인인지 여부를 반환하는 함수 (반환 타입: Promise<boolean>)
    fetchIsExpertOnline('배수진');
    
    return [];
}


function solution(type, id, listener) {
    return {
        type,
        id,
        onEvent(event) {
            listener(event);
        },
        addChild(node) {},
        removeChild(node) {},
    }
}