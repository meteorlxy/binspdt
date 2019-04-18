<template>
  <VProgressCircular
    :rotate="360"
    :size="120"
    :width="10"
    :value="value * 100"
    :color="value > 0.8 ? 'orange' : value > 0.4 ? 'blue' : 'teal'"
  >
    {{ $helpers.floatToPercent(value) }}
  </VProgressCircular>
</template>

<script lang="ts">
import { Component, Vue, Prop } from 'vue-property-decorator'

@Component
export default class SimilarityCircular extends Vue {
  @Prop({
    type: Number,
    required: true,
  }) value!: number
}
</script>
