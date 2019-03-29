<template>
  <VLayout
    row
    wrap>
    <VFlex
      xs12
      md4>
      <VLayout
        column
        wrap>
        <VFlex>
          <VCard>
            <VCardTitle>
              <VBtn
                color="grey"
                title="Back To Analyses List"
                :to="{ name: 'dashboard.analyses' }"
                exact
                icon
                flat>
                <VIcon>arrow_back</VIcon>
              </VBtn>

              <VSpacer/>

              <VProgressCircular
                v-show="isLoading"
                color="primary"
                indeterminate/>
            </VCardTitle>

            <VCardText class="text-xs-center">
              <VProgressCircular
                :rotate="360"
                :size="120"
                :width="10"
                :value="overallSimilarity * 100"
                :color="overallSimilarity > 0.8 ? 'orange' : overallSimilarity > 0.4 ? 'blue' : 'teal'">
                {{ $helpers.floatToPercent(overallSimilarity) }}
              </VProgressCircular>
            </VCardText>

            <VCardText class="text-xs-center pb-4">
              <div class="headline">
                Overall Similarity
              </div>

              <div class="grey--text">
                Match the most similar functions in two modules
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

            <VCardText class="mt-3">
              <VSlider
                :value="analysis.params.k"
                readonly
                :max="6"
                :min="0"
                :step="1"
                label="Call Depth k"
                ticks="always"
                thumb-label="always"
                hint="Function call depth used in analysis. [default: 2]"
                persistent-hint>
                <span
                  slot="append"
                  class="ml-2">
                  {{ analysis.params.k }}
                </span>
              </VSlider>
            </VCardText>

            <VCardText>
              <VTextField
                :value="algorithm.text"
                readonly
                label="Matching Algorithm"
                hint="Matching algorithm used to match similar functions. [default: km]"
                persistent-hint/>
            </VCardText>
          </VCard>
        </VFlex>
      </VLayout>
    </VFlex>

    <VFlex
      xs12
      md8>
      <VLayout
        row
        wrap>
        <VFlex
          xs12
          md6>
          <ModuleDetailsCard
            :data="moduleA"
            :fields-hide="['comment', 'exporter', 'import_time']">
            Module A
          </ModuleDetailsCard>
        </VFlex>

        <VFlex
          xs12
          md6>
          <ModuleDetailsCard
            :data="moduleB"
            :fields-hide="['comment', 'exporter', 'import_time']">
            Module B
          </ModuleDetailsCard>
        </VFlex>

        <VFlex xs12>
          <VCard>
            <VCardTitle>
              <div>
                <div class="headline">
                  <slot>Matched Functions</slot>
                </div>

                <div class="grey--text">
                  List of functions similarity
                </div>
              </div>
            </VCardTitle>

            <VDataTable
              :headers="tableHeaders"
              :items="tableItems">
              <template
                slot="items"
                slot-scope="props">
                <tr @click="props.expanded = !props.expanded">
                  <td>{{ $helpers.decToHex(props.item.module_1_function_address) }}</td>
                  <td>{{ $helpers.decToHex(props.item.module_2_function_address) }}</td>
                  <td>{{ $helpers.floatToPercent(props.item.similarity) }}</td>
                </tr>
              </template>

              <template
                slot="expand"
                slot-scope="props">
                <VLayout
                  class="pa-3"
                  row>
                  <VFlex xs6>
                    <VSubheader>
                      API Calls in Module A Function
                    </VSubheader>

                    <VList dense>
                      <VListTile
                        v-for="(val, index) in props.item.module_1_function_api"
                        :key="index">
                        <VListTileTitle>
                          {{ val }}
                        </VListTileTitle>
                      </VListTile>
                    </VList>
                  </VFlex>

                  <VFlex xs6>
                    <VSubheader>
                      API Calls in Module B Function
                    </VSubheader>

                    <VList dense>
                      <VListTile
                        v-for="(val, index) in props.item.module_2_function_api"
                        :key="index">
                        <VListTileTitle>
                          {{ val }}
                        </VListTileTitle>
                      </VListTile>
                    </VList>
                  </VFlex>
                </VLayout>
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
import { Component, Vue, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component({
  components: {
    ModuleDetailsCard,
  },
})
export default class APISetResult extends Vue {
  @namespace('binary/modules').Action('getModule') getModule
  @namespace('binary/analyses').State('methods') methods
  @namespace('binary/analyses').State('algorithms') algorithms

  @Prop({
    type: Object,
    required: true,
  }) analysis!: any

  isLoading: boolean = false

  moduleA: any = {}
  moduleB: any = {}

  overallSimilarity: number = 0

  get method () {
    return this.methods.find(item => item.name === this.analysis.method)
  }

  get algorithm () {
    return this.algorithms.find(item => item.name === this.analysis.params.algorithm)
  }

  get tableItems () {
    return this.analysis.data.matched_functions.map((item, index) => ({
      id: index,
      ...item,
    }))
  }

  get tableHeaders () {
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
      this.overallSimilarity = this.analysis.data['overall_similarity']
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
