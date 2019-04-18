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
          :max="7"
          :min="1"
          :step="1"
          label="Parameter k"
          ticks="always"
          thumb-label="always"
          hint="Length of subsequence when generating k-grams. [default: 1]"
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
        <VCheckbox
          v-model="params['match_sequence']"
          :false-value="false"
          :true-value="true"
          class="my-0"
          :readonly="readonly"
          label="Match functions with read-write sequence"
        />

        <VCheckbox
          v-model="params['match_vector']"
          :false-value="false"
          :true-value="true"
          class="my-0"
          :readonly="readonly"
          label="Match functions with read-write vector"
        />

        <VSelect
          v-if="params['match_sequence'] || params['match_vector']"
          v-model="params['algorithm']"
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
export default class KeyReadWriteParams extends Vue {
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

  internalParams: {
    'k': number,
    'match_sequence': boolean,
    'match_vector': boolean,
    'algorithm': string,
  } = {
    'k': 1,
    'match_sequence': false,
    'match_vector': false,
    'algorithm': 'km',
  }

  internalIsValid: boolean = true

  get params () {
    return this.internalParams
  }

  set params (params) {
    this.internalIsValid = Number.isInteger(params['k']) && params['k'] >= 1 && params['k'] <= 7 &&
      Boolean(this.algorithms.find(item => item.name === params['algorithm'])) &&
      typeof params['match_sequence'] === 'boolean' &&
      typeof params['match_vector'] === 'boolean'
    this.internalParams = params
    this.$emit('input', params)
    this.$emit('update:isValid', this.internalIsValid)
  }

  created () {
    if ('algorithm' in this.value && 'match_sequence' in this.value && 'match_vector' in this.value) {
      this.params = this.value
    } else {
      this.params = this.internalParams
    }
  }
}
</script>
