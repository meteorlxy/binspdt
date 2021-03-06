<template>
  <VLayout
    row
    wrap
  >
    <VFlex xs12>
      <VCardText class="mt-3">
        <VSlider
          v-model="params.k"
          :readonly="readonly"
          :max="6"
          :min="0"
          :step="1"
          label="Call Depth k"
          ticks="always"
          thumb-label="always"
          hint="Function call depth used in analysis. [default: 2]"
          persistent-hint
        >
          <template v-slot:append>
            <span class="ml-2">
              {{ params.k }}
            </span>
          </template>
        </VSlider>
      </VCardText>
    </VFlex>

    <VFlex xs12>
      <VCardText>
        <VSelect
          v-model="params.algorithm"
          :readonly="readonly"
          :items="algorithms"
          :item-text="item => item.text"
          :item-value="item => item.name"
          label="Matching Algorithm"
          hint="Matching algorithm used to match similar functions. [default: km]"
          persistent-hint
        />
      </VCardText>
    </VFlex>
  </VLayout>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component
export default class APISetParams extends Vue {
  @namespace('binary/analyses').State('functionMatchAlgorithms') algorithms

  @Prop({
    type: Object,
    required: true,
  }) value!: any

  @Prop({
    required: false,
    default: true,
  }) isValid!: boolean

  @Prop({
    type: Boolean,
    required: false,
    default: false,
  }) readonly!: boolean

  internalParams = {
    'k': 2,
    'algorithm': 'km',
  }

  internalIsValid = true

  get params () {
    return this.internalParams
  }

  set params (params) {
    this.internalIsValid = Number.isInteger(params['k']) && params['k'] >= 0 && params['k'] <= 6 &&
      Boolean(this.algorithms.find(item => item.name === params['algorithm']))
    this.internalParams = params
    this.$emit('input', params)
    this.$emit('update:isValid', this.internalIsValid)
  }

  created () {
    if ('k' in this.value && 'algorithm' in this.value) {
      this.params = this.value
    } else {
      this.params = this.internalParams
    }
  }
}
</script>
