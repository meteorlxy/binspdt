<template>
  <VNavigationDrawer
    app
    fixed
    clipped
    :mobile-break-point="1264"
    :value="value"
    @input="handleInput"
  >
    <VList class="pt-0">
      <VListTile class="py-2">
        <VListTileAvatar color="indigo">
          <span class="white--text headline">
            {{ username.charAt(0).toUpperCase() }}
          </span>
        </VListTileAvatar>

        <VListTileContent>
          <VListTileTitle>{{ username }}</VListTileTitle>

          <VListTileSubTitle>Welcome to BinSPDT!</VListTileSubTitle>
        </VListTileContent>
      </VListTile>

      <VDivider class="mb-2" />

      <VListTile
        :to="{ name: 'dashboard' }"
        :exact="true"
      >
        <VListTileAction>
          <VIcon>dashboard</VIcon>
        </VListTileAction>

        <VListTileContent>
          <VListTileTitle>Dashboard</VListTileTitle>
        </VListTileContent>
      </VListTile>

      <VListTile
        :to="{ name: 'dashboard.modules' }"
        :exact="false"
      >
        <VListTileAction>
          <VIcon>developer_board</VIcon>
        </VListTileAction>

        <VListTileContent>
          <VListTileTitle>Modules</VListTileTitle>
        </VListTileContent>
      </VListTile>

      <VListTile
        :to="{ name: 'dashboard.analyses' }"
        :exact="false"
      >
        <VListTileAction>
          <VIcon>timeline</VIcon>
        </VListTileAction>

        <VListTileContent>
          <VListTileTitle>Analyses</VListTileTitle>
        </VListTileContent>
      </VListTile>

      <VListGroup no-action>
        <template v-slot:activator>
          <VListTile>
            <VListTileAction>
              <VIcon>local_library</VIcon>
            </VListTileAction>

            <VListTileContent>
              <VListTileTitle>Wiki</VListTileTitle>
            </VListTileContent>
          </VListTile>
        </template>

        <VListTile
          :to="{ name: 'dashboard.wiki.key-read-write' }"
          :exact="true"
        >
          <VListTileContent>
            <VListTileTitle>Key Read-Write</VListTileTitle>
          </VListTileContent>
        </VListTile>

        <VListTile
          :to="{ name: 'dashboard.wiki.api-set' }"
          :exact="true"
        >
          <VListTileContent>
            <VListTileTitle>API Set</VListTileTitle>
          </VListTileContent>
        </VListTile>

        <VListTile
          :to="{ name: 'dashboard.wiki.k-gram' }"
          :exact="true"
        >
          <VListTileContent>
            <VListTileTitle>K-Gram</VListTileTitle>
          </VListTileContent>
        </VListTile>

        <VListTile
          :to="{ name: 'dashboard.wiki.api-frequency' }"
          :exact="true"
        >
          <VListTileContent>
            <VListTileTitle>API Frequency</VListTileTitle>
          </VListTileContent>
        </VListTile>
      </VListGroup>
    </VList>
  </VNavigationDrawer>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component
export default class TheSidebar extends Vue {
  @Prop(Boolean) value!: boolean | null

  @namespace('website/user').State('username') username

  handleInput (payload: boolean | null): void {
    this.$emit('input', payload)
  }
}
</script>
