<template>
  <VLayout
    row
    wrap
  >
    <VFlex
      xs12
      md4
    >
      <VLayout
        column
        wrap
      >
        <VFlex>
          <VCard>
            <VCardTitle>
              <VBtn
                color="grey"
                title="Back To Analyses List"
                :to="{ name: 'dashboard.analyses' }"
                exact
                icon
                flat
              >
                <VIcon>arrow_back</VIcon>
              </VBtn>

              <VSpacer />

              <VProgressCircular
                v-show="isLoading"
                color="primary"
                indeterminate
              />
            </VCardTitle>

            <VCardText class="text-xs-center">
              <SimilarityCircular :value="overallSimilarity" />
            </VCardText>

            <VCardText class="text-xs-center pb-4">
              <div class="headline">
                Overall Similarity
              </div>
            </VCardText>
          </VCard>
        </VFlex>

        <VFlex>
          <VCard>
            <VCardTitle>
              <div>
                <div class="headline">
                  Parameters
                </div>

                <div class="grey--text">
                  Method: {{ method.text }}
                </div>
              </div>
            </VCardTitle>

            <KeyReadWriteParams
              :value="analysis['params']"
              readonly
            />
          </VCard>
        </VFlex>
      </VLayout>
    </VFlex>

    <VFlex
      xs12
      md8
    >
      <VLayout
        row
        wrap
      >
        <VFlex
          xs12
          md6
        >
          <ModuleDetailsCard
            :data="moduleA"
            :fields-hide="['comment', 'exporter', 'import_time']"
          >
            Module A
          </ModuleDetailsCard>
        </VFlex>

        <VFlex
          xs12
          md6
        >
          <ModuleDetailsCard
            :data="moduleB"
            :fields-hide="['comment', 'exporter', 'import_time']"
          >
            Module B
          </ModuleDetailsCard>
        </VFlex>

        <VFlex xs12>
          <VCard>
            <VCardTitle>
              <VLayout
                row
                wrap
              >
                <VFlex
                  xs="10"
                  sm="11"
                >
                  <div class="headline">
                    <slot>Read-Write Vector</slot>
                  </div>

                  <div class="grey--text">
                    Functions similarity of Read-Write Vector
                  </div>
                </VFlex>

                <VFlex
                  xs="2"
                  sm="1"
                  class="text-xs-right"
                >
                  <VSwitch
                    v-model="vectorAtoB"
                    class="d-inline-block"
                    :title="vectorAtoB ? 'A to B' : 'B to A'"
                  />
                </VFlex>
              </VLayout>
            </VCardTitle>

            <VCardText v-if="matchedVector">
              <p>
                Matched similarity: {{ $helpers.floatToPercent(matchedVector['similarity']) }} (filtered {{ $helpers.floatToPercent(matchedVector['similarity_filtered']) }})
              </p>
              <p>
                Matched similarity A to B: {{ $helpers.floatToPercent(matchedVector['similarity_1_to_2']) }} (filtered {{ $helpers.floatToPercent(matchedVector['similarity_1_to_2_filtered']) }})
              </p>
              <p>
                Matched similarity B to A: {{ $helpers.floatToPercent(matchedVector['similarity_2_to_1']) }} (filtered {{ $helpers.floatToPercent(matchedVector['similarity_2_to_1_filtered']) }})
              </p>
            </VCardText>

            <VDataTable
              :headers="tableVectorHeaders"
              :items="tableVectorItems"
              :loading="isLoading"
              :rows-per-page-items="[10, 20, 50, 100]"
            >
              <template v-slot:items="props">
                <tr>
                  <td>{{ $helpers.decToHex(props.item['module_1_function_address']) }}</td>
                  <td>{{ $helpers.decToHex(props.item['module_2_function_address']) }}</td>
                  <td>{{ $helpers.floatToPercent(props.item['similarity']) }}</td>
                </tr>
              </template>
            </VDataTable>
          </VCard>
        </VFlex>

        <VFlex xs12>
          <VCard>
            <VCardTitle>
              <VLayout
                row
                wrap
              >
                <VFlex
                  xs="10"
                  sm="11"
                >
                  <div class="headline">
                    <slot>Read-Write Sequence</slot>
                  </div>

                  <div class="grey--text">
                    Functions similarity of Read-Write Sequence
                  </div>
                </VFlex>

                <VFlex
                  xs="2"
                  sm="1"
                  class="text-xs-right"
                >
                  <VSwitch
                    v-model="sequenceAtoB"
                    class="d-inline-block"
                    :title="sequenceAtoB ? 'A to B' : 'B to A'"
                  />
                </VFlex>
              </VLayout>
            </VCardTitle>

            <VCardText v-if="matchedSequence">
              <p>
                Matched similarity: {{ $helpers.floatToPercent(matchedSequence['similarity']) }} (filtered {{ $helpers.floatToPercent(matchedSequence['similarity_filtered']) }})
              </p>
              <p>
                Matched similarity A to B: {{ $helpers.floatToPercent(matchedSequence['similarity_1_to_2']) }} (filtered {{ $helpers.floatToPercent(matchedSequence['similarity_1_to_2_filtered']) }})
              </p>
              <p>
                Matched similarity B to A: {{ $helpers.floatToPercent(matchedSequence['similarity_2_to_1']) }} (filtered {{ $helpers.floatToPercent(matchedSequence['similarity_2_to_1_filtered']) }})
              </p>
            </VCardText>

            <VDataTable
              :headers="tableSequenceHeaders"
              :items="tableSequenceItems"
              :loading="isLoading"
              :rows-per-page-items="[10, 20, 50, 100]"
            >
              <template v-slot:items="props">
                <tr>
                  <td>{{ $helpers.decToHex(props.item['module_1_function_address']) }}</td>
                  <td>{{ $helpers.decToHex(props.item['module_2_function_address']) }}</td>
                  <td>{{ $helpers.floatToPercent(props.item['similarity']) }}</td>
                </tr>
              </template>
            </VDataTable>
          </VCard>
        </VFlex>
      </VLayout>
    </VFlex>
  </VLayout>
</template>

<script lang="ts">
import ModuleDetailsCard from '@/components/dashboard/ModuleDetailsCard.vue'
import SimilarityCircular from '../SimilarityCircular.vue'
import KeyReadWriteParams from './KeyReadWriteParams.vue'
import { Component, Vue, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component({
  components: {
    ModuleDetailsCard,
    SimilarityCircular,
    KeyReadWriteParams,
  },
})
export default class KeyReadWriteResult extends Vue {
  @namespace('binary/modules').Action('getModule') getModule
  @namespace('binary/analyses').State('methods') methods
  @namespace('binary/analyses').State('functionMatchAlgorithms') algorithms

  @Prop({
    type: Object,
    required: true,
  }) analysis!: any

  isLoading: boolean = false

  moduleA: any = {}
  moduleB: any = {}

  overallSimilarity: number = 0

  sequenceAtoB: boolean = true
  vectorAtoB: boolean = true

  get method () {
    return this.methods.find(item => item.name === this.analysis['method'])
  }

  get algorithm () {
    return this.algorithms.find(item => item.name === this.analysis['params']['algorithm'])
  }

  get matchedSequence () {
    return this.analysis['result']['matched_sequence'] || null
  }

  get matchedVector () {
    return this.analysis['result']['matched_vector'] || null
  }

  get functionsSimilarityAtoB () {
    return Object.entries(this.analysis['result']['module_1_funcs']).map(([addr, item], index) => {
      const max = Object.entries(item).reduce((acc, cur) => {
        if (cur[1]['similarity_sequence'] > acc['sequence']['sim']) {
          acc['sequence']['addr'] = cur[0]
          acc['sequence']['sim'] = cur[1]['similarity_sequence']
        }
        if (cur[1]['similarity_vector'] > acc['vector']['sim']) {
          acc['vector']['addr'] = cur[0]
          acc['vector']['sim'] = cur[1]['similarity_vector']
        }
        return acc
      }, {
        'sequence': {
          'addr': '',
          'sim': 0,
        },
        'vector': {
          'addr': '',
          'sim': 0,
        },
      })
      return {
        'sequence': {
          id: index,
          'module_1_function_address': addr,
          'module_2_function_address': max['sequence']['addr'],
          'similarity': max['sequence']['sim'],
        },
        'vector': {
          id: index,
          'module_1_function_address': addr,
          'module_2_function_address': max['vector']['addr'],
          'similarity': max['vector']['sim'],
        },
      }
    })
  }

  get functionsSimilarityBtoA () {
    return Object.entries(this.analysis['result']['module_2_funcs']).map(([addr, item], index) => {
      const max = Object.entries(item).reduce((acc, cur) => {
        if (cur[1]['similarity_sequence'] > acc['sequence']['sim']) {
          acc['sequence']['addr'] = cur[0]
          acc['sequence']['sim'] = cur[1]['similarity_sequence']
        }
        if (cur[1]['similarity_vector'] > acc['vector']['sim']) {
          acc['vector']['addr'] = cur[0]
          acc['vector']['sim'] = cur[1]['similarity_vector']
        }
        return acc
      }, {
        'sequence': {
          'addr': '',
          'sim': 0,
        },
        'vector': {
          'addr': '',
          'sim': 0,
        },
      })
      return {
        'sequence': {
          id: index,
          'module_1_function_address': max['sequence']['addr'],
          'module_2_function_address': addr,
          'similarity': max['sequence']['sim'],
        },
        'vector': {
          id: index,
          'module_1_function_address': max['vector']['addr'],
          'module_2_function_address': addr,
          'similarity': max['vector']['sim'],
        },
      }
    })
  }

  get tableSequenceItems () {
    const source = this.sequenceAtoB ? this.functionsSimilarityAtoB : this.functionsSimilarityBtoA
    return source.map(item => item['sequence'])
  }

  get tableSequenceHeaders () {
    return [
      {
        text: 'Module A Function Address',
        value: 'module_1_function_address',
      },
      {
        text: 'Module B Function Address',
        value: 'module_2_function_address',
      },
      {
        text: 'Similarity',
        value: 'similarity',
      },
    ]
  }

  get tableVectorItems () {
    const source = this.vectorAtoB ? this.functionsSimilarityAtoB : this.functionsSimilarityBtoA
    return source.map(item => item['vector'])
  }

  get tableVectorHeaders () {
    return [
      {
        text: 'Module A Function Address',
        value: 'module_1_function_address',
      },
      {
        text: 'Module B Function Address',
        value: 'module_2_function_address',
      },
      {
        text: 'Similarity',
        value: 'similarity',
      },
    ]
  }

  async created () {
    await this.handleGetModule()
  }

  mounted () {
    setTimeout(() => {
      this.overallSimilarity = this.analysis['result']['overall_similarity']
    }, 500)
  }

  async handleGetModule () {
    try {
      this.isLoading = true
      const [responseA, responseB] = await Promise.all([
        this.getModule({ id: this.analysis['module_1_id'] }),
        this.getModule({ id: this.analysis['module_2_id'] }),
      ])
      this.moduleA = responseA.data.data
      this.moduleB = responseB.data.data
    } catch (error) {

    } finally {
      this.isLoading = false
    }
  }
}
</script>
