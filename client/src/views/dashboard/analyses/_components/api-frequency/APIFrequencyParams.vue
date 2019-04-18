<template>
  <VLayout
    row
    wrap
  >
    <VFlex xs12>
      <VCardText>
        No parameters available for this method.
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
  }

  internalIsValid = true

  get params () {
    return this.internalParams
  }

  set params (params) {
    this.internalIsValid = Object.keys(params).length === 0
    this.internalParams = params
    this.$emit('input', params)
    this.$emit('update:isValid', this.internalIsValid)
  }

  created () {
    if (Object.keys(this.value).length === 0) {
      this.params = this.value
    } else {
      this.params = this.internalParams
    }
  }
}
</script>
