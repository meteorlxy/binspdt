<template>
  <PageLoading v-if="isLoadingModule"/>

  <VLayout
    v-else
    row
    wrap>
    <VFlex
      xs12
      md4>
      <VLayout
        column
        wrap>
        <VFlex>
          <ModuleDetailsCard
            :data="moduleData"
            show-all>
            Info
          </ModuleDetailsCard>
        </VFlex>
      </VLayout>
    </VFlex>

    <VFlex
      xs12
      md8>
      <VLayout
        row
        wrap>
        <VFlex xs12>
          <VCard>
            <VCardTitle>
              <div>
                <div class="headline">
                  <slot>Functions</slot>
                </div>

                <div class="grey--text">
                  All functions of this module
                </div>
              </div>
            </VCardTitle>

            <VDataTable
              :headers="functionTableHeaders"
              :items="functionTableItems"
              :loading="isLoadingFunctions"
              :rows-per-page-items="[10, 20, 50, 100]">
              <template v-slot:items="props">
                <tr @click="handleGetFunctionBasicBlocks(props.item)">
                  <td>{{ $helpers.decToHex(props.item.address) }}</td>
                  <td>{{ props.item.name }}</td>
                  <td>{{ props.item.module_name }}</td>
                  <td>{{ props.item.type }}</td>
                </tr>
              </template>
            </VDataTable>
          </VCard>
        </VFlex>

        <VFlex
          v-show="displayFunction"
          xs12>
          <VCard>
            <VCardTitle>
              <div>
                <div class="headline">
                  <slot>Basic Blocks</slot>
                </div>

                <div class="grey--text">
                  All basic blocks of function @{{ $helpers.decToHex(displayFunction) }}
                </div>
              </div>
            </VCardTitle>

            <VDataTable
              :headers="basicBlockTableHeaders"
              :items="basicBlockTableItems"
              :loading="isLoadingBasicBlocks"
              :rows-per-page-items="[10, 20, 50, 100]">
              <template v-slot:items="props">
                <tr @click="handleGetBasicBlockInstructions(props.item)">
                  <td>{{ $helpers.decToHex(props.item.address) }}</td>
                  <td>{{ props.item.id }}</td>
                  <td>{{ $helpers.decToHex(props.item.parent_function) }}</td>
                </tr>
              </template>
            </VDataTable>
          </VCard>
        </VFlex>

        <VFlex
          v-show="displayBasicBlock"
          xs12>
          <VCard>
            <VCardTitle>
              <div>
                <div class="headline">
                  <slot>Instructions</slot>
                </div>

                <div class="grey--text">
                  All instructions of basic block @{{ $helpers.decToHex(displayBasicBlock) }}
                </div>
              </div>
            </VCardTitle>

            <VDataTable
              :headers="instructionTableHeaders"
              :items="instructionTableItems"
              :loading="isLoadingInstructions"
              :rows-per-page-items="[10, 20, 50, 100]">
              <template v-slot:items="props">
                <tr>
                  <td>{{ $helpers.decToHex(props.item.address) }}</td>
                  <td>{{ props.item.mnemonic }}</td>
                  <td>{{ props.item.operands[0] }}</td>
                  <td>{{ props.item.operands[1] }}</td>
                  <td>{{ props.item.operands[2] }}</td>
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
import PageLoading from '@/components/PageLoading.vue'
import ModuleDetailsCard from '@/components/dashboard/ModuleDetailsCard.vue'
import { Component, Vue, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component({
  components: {
    ModuleDetailsCard,
    PageLoading,
  },
})
export default class ModulesDetails extends Vue {
  @namespace('binary/modules').Action('getModule') getModule
  @namespace('binary/modules').Action('getModuleFunctions') getModuleFunctions
  @namespace('binary/modules').Action('getFunctionBasicBlocks') getFunctionBasicBlocks
  @namespace('binary/modules').Action('getBasicBlockInstructions') getBasicBlockInstructions

  @Prop({
    type: Number,
    required: true,
  }) id!: number

  isLoadingModule: boolean = false
  isLoadingFunctions: boolean = false
  isLoadingBasicBlocks: boolean = false
  isLoadingInstructions: boolean = false

  moduleData: any = {}
  moduleFunctions: any = []

  functionTableItems: any = []
  basicBlockTableItems: any = []
  instructionTableItems: any = []

  displayFunction: any = null
  displayBasicBlock: any = null

  get functionTableHeaders () {
    return [
      { text: 'Address', value: 'address' },
      { text: 'Name', value: 'name' },
      { text: 'Module', value: 'module_name' },
      { text: 'Type', value: 'type' },
    ]
  }

  get basicBlockTableHeaders () {
    return [
      { text: 'Address', value: 'address' },
      { text: 'ID', value: 'id' },
      { text: 'Parent Function', value: 'parent_function' },
    ]
  }

  get instructionTableHeaders () {
    return [
      { text: 'Address', value: 'address' },
      { text: 'Mnemonic', value: 'mnemonic' },
      { text: 'Operand 1', sortable: false },
      { text: 'Operand 2', sortable: false },
      { text: 'Operand 3', sortable: false },
    ]
  }

  created () {
    this.handleGetModule()
    this.handleGetModuleFunctions()
  }

  async handleLoadChildren (item) {
    if (item.type === 'function') {
      return this.handleGetFunctionBasicBlocks(item)
    } else if (item.type === 'basic_block') {
      return this.handleGetBasicBlockInstructions(item)
    }
  }

  async handleGetModule () {
    try {
      this.isLoadingModule = true
      const response = await this.getModule({
        id: this.id,
      })
      this.moduleData = response.data.data
    } catch (error) {

    } finally {
      this.isLoadingModule = false
    }
  }

  async handleGetModuleFunctions () {
    try {
      this.isLoadingFunctions = true
      const response = await this.getModuleFunctions({
        moduleId: this.id,
      })
      this.functionTableItems = response.data.data
    } catch (error) {

    } finally {
      this.isLoadingFunctions = false
    }
  }

  async handleGetFunctionBasicBlocks (item) {
    try {
      this.isLoadingBasicBlocks = true
      this.displayBasicBlock = null
      const response = await this.getFunctionBasicBlocks({
        moduleId: this.id,
        functionAddress: item.address,
      })
      this.displayFunction = item.address
      this.basicBlockTableItems = response.data.data
    } catch (error) {

    } finally {
      this.isLoadingBasicBlocks = false
    }
  }

  async handleGetBasicBlockInstructions (item) {
    try {
      this.isLoadingInstructions = true
      const response = await this.getBasicBlockInstructions({
        moduleId: this.id,
        functionAddress: item['parent_function'],
        basicBlockId: item.id,
      })
      this.displayBasicBlock = item.address
      this.instructionTableItems = response.data.data
    } catch (error) {

    } finally {
      this.isLoadingInstructions = false
    }
  }
}
</script>
