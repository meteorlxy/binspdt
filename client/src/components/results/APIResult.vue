<template>
  <article>
    <section class="overall-similarity">
      <ElProgress
        type="circle"
        :percentage="overallPercentage"
        :color="overallColor"/>

      <p>{{ $t('binary.analysis.api.result.overall_similarity') }}</p>
    </section>
  </article>
</template>

<script>
export default {
  name: 'APIResult',
  props: {
    data: {
      type: [Object],
      required: true
    }
  },
  computed: {
    overallPercentage () {
      return this.data.details.overall_similarity * 100
    },
    overallColor () {
      if (this.overallPercentage >= 70) {
        return '#8e71c7'
      }
      if (this.overallPercentage >= 40) {
        return '#20a0ff'
      }
      return '#13ce66'
    }
  }
}
</script>

<style lang="scss" scoped>
.analysis-result {
  text-align: center;
  box-shadow: 1px 1px 2px #999;
  padding: 2.5rem 1.5rem;
  .title {
    font-size: 1.5rem;
    margin: 0.5rem 0;
  }
  .subtitle {
    color: #999;
    font-size: 1rem;
    font-weight: normal;
  }
  .overall-similarity {
    text-align: center;
  }
}
</style>
