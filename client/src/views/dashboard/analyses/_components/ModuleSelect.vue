<template>
  <div>
    <VAutocomplete
      v-model="selectedModule"
      :label="label"
      :hint="hint"
      :persistent-hint="persistentHint"
      :clearable="clearable && !hasConfirmed"
      :prepend-icon="prependIcon"
      :append-icon="hasConfirmed ? 'check' : ''"
      :search-input.sync="search"
      :loading="isLoading"
      :error-messages="errorMessages"
      :readonly="hasConfirmed"
      :success="hasConfirmed"
      :items="modules"
      :item-text="item => `#${item.id} ${item.name}`"
      :item-value="item => item">
      <template
        v-if="hasConfirmed"
        v-slot:append-outer>
        <VSlideXReverseTransition>
          <VIcon @click="hasConfirmed = false">
            edit
          </VIcon>
        </VSlideXReverseTransition>
      </template>

      <template v-slot:no-data>
        <VListTile>
          <template v-if="hasLoaded">
            No matched modules
          </template>

          <template v-else>
            Type to search modules
          </template>
        </VListTile>
      </template>
    </VAutocomplete>

    <VExpandTransition v-if="selectedModule && !hasConfirmed">
      <VList class="my-3 ml-4 grey lighten-3">
        <VListTile>
          <VListTileContent>
            <VListTileTitle>
              Module ID
            </VListTileTitle>

            <VListTileSubTitle>
              {{ selectedModule.id }}
            </VListTileSubTitle>
          </VListTileContent>
        </VListTile>

        <VListTile>
          <VListTileContent>
            <VListTileTitle>
              Module Name
            </VListTileTitle>

            <VListTileSubTitle>
              {{ selectedModule.name }}
            </VListTileSubTitle>
          </VListTileContent>
        </VListTile>

        <VListTile>
          <VListTileContent>
            <VListTileTitle>
              Architecture
            </VListTileTitle>

            <VListTileSubTitle>
              {{ selectedModule.architecture }}
            </VListTileSubTitle>
          </VListTileContent>
        </VListTile>

        <VListTile>
          <VListTileContent>
            <VListTileTitle>
              MD5
            </VListTileTitle>

            <VListTileSubTitle>
              {{ selectedModule.md5 }}
            </VListTileSubTitle>
          </VListTileContent>
        </VListTile>

        <VListTile>
          <VListTileContent>
            <VListTileTitle>
              SHA1
            </VListTileTitle>

            <VListTileSubTitle>
              {{ selectedModule.sha1 }}
            </VListTileSubTitle>
          </VListTileContent>
        </VListTile>

        <VListTile>
          <VListTileContent>
            <VListTileTitle>
              Exporter
            </VListTileTitle>

            <VListTileSubTitle>
              {{ selectedModule.exporter }}
            </VListTileSubTitle>
          </VListTileContent>
        </VListTile>

        <VListTile>
          <VListTileContent>
            <VListTileTitle>
              Upload Time
            </VListTileTitle>

            <VListTileSubTitle>
              {{ selectedModule.import_time }}
            </VListTileSubTitle>
          </VListTileContent>
        </VListTile>

        <VListTile>
          <VListTileContent>
            <VBtn
              class="ml-0"
              color="success"
              @click="hasConfirmed = true">
              <VIcon left>
                check
              </VIcon>
              Confirm
            </VBtn>
          </VListTileContent>
        </VListTile>
      </VList>
    </VExpandTransition>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop, Watch } from 'vue-property-decorator'
import { namespace } from 'vuex-class'
import { getModules } from '@/api/binary/modules'

@Component
export default class ModuleSelect extends Vue {
  @Prop({ type: String, required: false, default: '' }) label!: string
  @Prop({ type: String, required: false, default: 'Type to search and select a module' }) hint!: string
  @Prop({ type: Boolean, required: false, default: true }) persistentHint!: boolean
  @Prop({ type: Boolean, required: false, default: true }) clearable!: boolean
  @Prop({ type: String, required: false, default: 'developer_board' }) prependIcon!: string
  @Prop({ required: false, default: null }) value!: any
  @Prop({ type: Boolean, required: false, default: false }) confirmed!: boolean

  @namespace('website/user').State('token') token

  modules: Array<any> = this.$store.state.binary.modules.modules.data

  errorMessages: Array<String> | String = []

  search: string | null = null
  isLoading: boolean = false
  hasLoaded: boolean = false
  hasConfirmed: boolean = false

  get selectedModule () {
    if (this.value === null) {
      return null
    }
    return this.modules.find(item => item.id === this.value.id)
  }

  set selectedModule (val) {
    this.$emit('input', val)
  }

  @Watch('search')
  onSearchChange (val: string) {
    if (val === '' || this.value !== null) {
      return false
    }
    this.handleGetModules()
  }

  @Watch('hasConfirmed')
  onHasConfirmedChange (val: boolean) {
    this.$emit('update:confirmed', val)
  }

  async handleGetModules () {
    if (this.hasConfirmed) {
      return false
    }

    if (this.search === null || this.search === '') {
      return false
    }

    try {
      this.isLoading = true
      this.errorMessages = []

      const response = await getModules({
        token: this.token,
        paginate: false,
        search: this.search,
      })

      this.modules = response.data.data
      this.hasLoaded = true
    } catch (error) {
      this.errorMessages = 'Something wrong when fetching modules. Please try again later'
    } finally {
      this.isLoading = false
    }
  }
}
</script>
