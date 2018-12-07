<template>
  <Sidebar>
    <SidebarBrand slot="top">
      <span class="fa-layers fa-fw ml-3 mr-2">
        <FaIcon
          icon="search"
          transform="grow-8" />

        <FaIcon
          :icon="['far', 'eye']"
          transform="shrink-8 up-2 left-1.5" />
      </span>

      <span class="brand-text font-weight-light">BinSPDT</span>
    </SidebarBrand>

    <SidebarUserPanel slot="sub">
      <FaIcon
        slot="image"
        class="text-white mx-2"
        :icon="['far', 'user']"
        transform="grow-4 down-4" />
      
      <span
        slot="info"
        class="text-white">
        Welcome, {{ username }} !
      </span>
    </SidebarUserPanel>

    <SidebarItem
      :to="{ name: 'dashboard' }"
      icon="tachometer-alt">
      Dashboard
    </SidebarItem>

    <SidebarItem
      :to="{ name: 'dashboard.modules' }"
      icon="cubes">
      Modules
    </SidebarItem>

    <SidebarItemTree
      :icon="['far', 'circle']">
      <template slot="title">
        Tree
      </template>
      
      <SidebarItem>
        Dashboard
      </SidebarItem>
    </SidebarItemTree>
  </Sidebar>
</template>

<script>
import { mapState } from 'vuex'
import Sidebar from '@/components/admin-lte/Sidebar'
import SidebarBrand from '@/components/admin-lte/SidebarBrand'
import SidebarItem from '@/components/admin-lte/SidebarItem'
import SidebarItemTree from '@/components/admin-lte/SidebarItemTree'
import SidebarUserPanel from '@/components/admin-lte/SidebarUserPanel'

export default {
  name: 'TheSidebar',

  components: {
    Sidebar,
    SidebarBrand,
    SidebarItem,
    SidebarItemTree,
    SidebarUserPanel,
  },

  computed: {
    ...mapState('website/user', [
      'username',
    ]),
  },
}
</script>

