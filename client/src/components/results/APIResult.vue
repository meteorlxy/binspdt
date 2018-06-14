<template>
  <article class="api-result">
    <section class="overall-similarity">
      <ElProgress
        type="circle"
        :percentage="overallPercentage"
        :color="overallColor"/>

      <p>{{ $t('binary.analysis.api.result.overall_similarity') }}: {{ `${overallPercentage}%` }}</p>

      <hr/>
    </section>

    <section class="analysis-params">
      <p>{{ $t('binary.analysis.api.call_depth') }}: {{ callDepth }}</p>

      <p>{{ $t('binary.analysis.api.match_algorithm') }}: {{ matchAlgorithm }}</p>
    </section>

    <section class="modules-details">
      <ElCollapse>
        <ElCollapseItem>
          <template slot="title">
            <i class="el-icon-document"></i>
            {{ $t('binary.results.result.module_details', { name: formatModuleName(moduleOne.id) }) }}
          </template>

          <div>{{ $t('binary.analysis.api.result.functions_with_api_count') }}: {{ moduleOneDetails.functions_with_api_count }}</div>

          <div>{{ $t('binary.modules.table.functions_count') }}: {{ moduleOneDetails.functions_count }}</div>

          <div>{{ $t('binary.modules.table.basic_blocks_count') }}: {{ moduleOneDetails.basic_blocks_count }}</div>

          <div>{{ $t('binary.modules.table.instructions_count') }}: {{ moduleOneDetails.instructions_count }}</div>
        </ElCollapseItem>

        <ElCollapseItem>
          <template slot="title">
            <i class="el-icon-document"></i>
            {{ $t('binary.results.result.module_details', { name: formatModuleName(moduleTwo.id) }) }}
          </template>

          <div>{{ $t('binary.analysis.api.result.functions_with_api_count') }}: {{ moduleTwoDetails.functions_with_api_count }}</div>

          <div>{{ $t('binary.modules.table.functions_count') }}: {{ moduleTwoDetails.functions_count }}</div>

          <div>{{ $t('binary.modules.table.basic_blocks_count') }}: {{ moduleTwoDetails.basic_blocks_count }}</div>

          <div>{{ $t('binary.modules.table.instructions_count') }}: {{ moduleTwoDetails.instructions_count }}</div>
        </ElCollapseItem>
      </ElCollapse>
    </section>

    <section class="similar-functions-lists">
      <ElCollapse>
        <ElCollapseItem>
          <template slot="title">
            <i class="el-icon-document"></i>
            {{ $t('binary.analysis.api.result.similar_functions') }} (TOP 50)
          </template>

          <ElTable
            :data="filteredMatchedFunctions"
            border
            stripe>
            <ElTableColumn type="expand">
              <template slot-scope="props">
                <ElForm label-position="left" inline class="table-details">
                  <ElFormItem
                    class="long label-long"
                    :label="$t('binary.analysis.api.result.function_api', { module: moduleOne.id })">
                    <span>{{ props.row.module_1_function_api.toString() }}</span>
                  </ElFormItem>

                  <hr/>

                  <ElFormItem
                    class="long label-long"
                    :label="$t('binary.analysis.api.result.function_api', { module: moduleTwo.id })">
                    <span>{{ props.row.module_2_function_api.toString() }}</span>
                  </ElFormItem>
                </ElForm>
              </template>
            </ElTableColumn>

            <ElTableColumn
              prop="module_1_function_address"
              :label="$t('binary.results.result.module_function_address', { name: moduleOne.id })"
            />

            <ElTableColumn
              prop="module_2_function_address"
              :label="$t('binary.results.result.module_function_address', { name: moduleTwo.id })"
            />

            <ElTableColumn
              prop="similarity"
              :label="$t('binary.results.result.similarity')"
              sortable/>
          </ElTable>
        </ElCollapseItem>
      </ElCollapse>
    </section>
  </article>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'APIResult',

  props: {
    data: {
      type: [Object],
      required: true
    }
  },

  data () {
    return {
      moduleOneDetails: {},
      moduleTwoDetails: {}
    }
  },

  computed: {
    ...mapState('binary/modules', [
      'modules'
    ]),

    overallPercentage () {
      return parseFloat((this.data.overall_similarity * 100).toFixed(2))
    },

    overallColor () {
      if (this.overallPercentage >= 70) {
        return '#8e71c7'
      }
      if (this.overallPercentage >= 40) {
        return '#20a0ff'
      }
      return '#13ce66'
    },

    callDepth () {
      return this.data.params.k
    },

    matchAlgorithm () {
      return this.data.params.algorithm
    },

    moduleOne () {
      return this.modules.find(m => m.id === this.data.module_1_details.id)
    },

    moduleTwo () {
      return this.modules.find(m => m.id === this.data.module_2_details.id)
    },

    filteredMatchedFunctions () {
      const filterFunc = item => item.similarity > 0
      const sortFunc = (a, b) => b.similarity - a.similarity

      const matchedFunctions = this.data.matched_functions
      const filteredMatchedFunctions = matchedFunctions.filter(filterFunc).sort(sortFunc).slice(0, 50)
      return filteredMatchedFunctions
    }
  },

  created () {
    this.getModuleDetails(this.moduleOne.id).then(details => {
      this.moduleOneDetails = {
        ...details,
        ...this.data.module_1_details
      }
    })
    this.getModuleDetails(this.moduleTwo.id).then(details => {
      this.moduleTwoDetails = {
        ...details,
        ...this.data.module_2_details
      }
    })
  },

  methods: {
    ...mapActions('binary/modules', {
      getModuleDetails: 'details'
    }),

    formatModuleName (moduleId) {
      return `[${moduleId}] ${this.modules.find(m => m.id === moduleId).name}`
    }
  }
}
</script>

<style lang="scss">
.api-result {
  .overall-similarity {
    text-align: center;
  }
  .analysis-params {
    text-align: center;
  }
  .el-form-item.long {
    .el-form-item__label {
      width: 200px;
    }
  }
}
</style>
