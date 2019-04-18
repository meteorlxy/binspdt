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
          :max="10"
          :min="1"
          :step="1"
          label="Parameter k"
          ticks="always"
          thumb-label="always"
          hint="Length of subsequence when generating k-grams. [default: 3]"
          persistent-hint
        >
          <template v-slot:append>
            <span
              class="ml-2"
            >
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
    'k': 3,
  }

  internalIsValid = true

  get params () {
    return this.internalParams
  }

  set params (params) {
    this.internalIsValid = Number.isInteger(params['k']) && params['k'] >= 1 && params['k'] <= 10
    this.internalParams = params
    this.$emit('input', params)
    this.$emit('update:isValid', this.internalIsValid)
  }

  created () {
    if ('k' in this.value) {
      this.params = this.value
    } else {
      this.params = this.internalParams
    }
  }
}
</script>
