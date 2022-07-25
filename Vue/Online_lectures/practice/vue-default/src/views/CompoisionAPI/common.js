import { computed, reactive, toRefs } from 'vue';

const plusCalculator = () => {
  let state = reactive({
    num1: 0,
    num2: 0,
    result: computed(() => state.num1 + state.num2),
  });

  return toRefs(state);
};

export { plusCalculator };
