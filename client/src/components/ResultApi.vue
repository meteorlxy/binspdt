<template>
  <div v-if="result">
    <p>{{ $t('binary.analysis.api.result', { result }) }}</p>
  </div>
</template>

<script>
export default {
  name: 'ResultApi',
  props: {
    result: {
      type: [Object, null],
      required: false,
      default: null
    }
  }
}
</script>
