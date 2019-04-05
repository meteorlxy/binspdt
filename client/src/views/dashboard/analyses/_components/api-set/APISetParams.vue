<template>
  <VLayout
    row
    wrap>
    <VFlex xs12>
      <VCardText class="mt-3 pl-0">
        <VSlider
          v-model="params.k"
          :max="6"
          :min="0"
          :step="1"
          label="Call Depth k"
          ticks="always"
          thumb-label="always"
          hint="Function call depth used in analysis. [default: 2]"
          persistent-hint>
          <template v-slot:prepend>
            <VBtn
              :to="{ name: 'dashboard.wiki.api-set' }"
              target="_blank"
              icon
              flat>
              <VIcon>
                help_outline
              </VIcon>
            </VBtn>
          </template>

          <template v-slot:append>
            <span
              class="ml-2">
              {{ params.k }}
            </span>
          </template>
        </VSlider>
      </VCardText>
    </VFlex>

    <VFlex xs12>
      <VCardText class="pl-0">
        <VSelect
          v-model="params.algorithm"
          :items="algorithms"
          :item-text="item => item.text"
          :item-value="item => item.name"
          label="Matching Algorithm"
          hint="Matching algorithm used to match similar functions. [default: km]"
          persistent-hint>
          <template v-slot:prepend>
            <VBtn
              :to="{ name: 'dashboard.wiki.api-set' }"
              target="_blank"
              icon
              flat>
              <VIcon>
                help_outline
              </VIcon>
            </VBtn>
          </template>
        </VSelect>
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
    required: false,
  }) value!: any

  @Prop({
    required: false,
    default: true,
  }) isValid!: boolean

  internalParams = {
    k: 2,
    algorithm: 'km',
  }

  internalIsValid = true

  get params () {
    return this.internalParams
  }

  set params (params) {
    this.internalIsValid = Number.isInteger(params.k) && params.k >= 0 && params.k <= 6
    this.internalParams = params
    this.$emit('input', params)
  }

  created () {
    this.params = this.internalParams
    this.$emit('update:isValid', this.internalIsValid)
  }
}
</script>
