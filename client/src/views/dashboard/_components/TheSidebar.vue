<template>
  <VNavigationDrawer
    app
    fixed
    clipped
    :mobile-break-point="1264"
    :value="value"
    @input="handleInput">
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

      <VDivider class="mb-2"/>

      <VListTile
        :to="{ name: 'dashboard' }"
        :exact="true">
        <VListTileAction>
          <VIcon>dashboard</VIcon>
        </VListTileAction>

        <VListTileContent>
          <VListTileTitle>Dashboard</VListTileTitle>
        </VListTileContent>
      </VListTile>

      <VListTile
        :to="{ name: 'dashboard.modules' }"
        :exact="false">
        <VListTileAction>
          <VIcon>developer_board</VIcon>
        </VListTileAction>

        <VListTileContent>
          <VListTileTitle>Modules</VListTileTitle>
        </VListTileContent>
      </VListTile>

      <VListTile
        :to="{ name: 'dashboard.analysis' }"
        :exact="false">
        <VListTileAction>
          <VIcon>timeline</VIcon>
        </VListTileAction>

        <VListTileContent>
          <VListTileTitle>Analysis</VListTileTitle>
        </VListTileContent>
      </VListTile>

      <VListGroup no-action>
        <VListTile slot="activator">
          <VListTileAction>
            <VIcon>local_library</VIcon>
          </VListTileAction>

          <VListTileContent>
            <VListTileTitle>Wiki</VListTileTitle>
          </VListTileContent>
        </VListTile>

        <VListTile
          :to="{ name: 'dashboard.wiki' }"
          :exact="true">
          <VListTileContent>
            <VListTileTitle>Wiki Index</VListTileTitle>
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
