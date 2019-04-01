<template>
  <VLayout
    row
    wrap>
    <VFlex xs12>
      <VCardText class="mt-3 pl-0">
        <VSlider
          v-model="params.k"
          :max="10"
          :min="1"
          :step="1"
          label="Parameter k"
          ticks="always"
          thumb-label="always"
          hint="Length of subsequence when generating k-grams. [default: 2]"
          persistent-hint>
          <template v-slot:prepend>
            <VBtn
              :to="{ name: 'dashboard.wiki.k-gram' }"
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
  </VLayout>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component
export default class KGramParams extends Vue {
  @namespace('binary/analyses').State('algorithms') algorithms

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
  }

  internalIsValid = true

  get params () {
    return this.internalParams
  }

  set params (params) {
    this.internalIsValid = Number.isInteger(params.k) && params.k >= 1 && params.k <= 10
    this.internalParams = params
    this.$emit('input', params)
  }

  created () {
    this.params = this.internalParams
    this.$emit('update:isValid', this.internalIsValid)
  }
}
</script>
