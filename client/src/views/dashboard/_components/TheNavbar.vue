<template>
  <Navbar>
    <NavbarItemGroup>
      <NavbarTogglerSidebar title="Toggle Sidebar" />

      <NavbarItem
        class="d-none d-sm-inline-block"
        to="/">
        Home
      </NavbarItem>

      <NavbarSearch />
    </NavbarItemGroup>

    <NavbarItemGroup position="right">
      <NavbarItem
        title="logout"
        @click.native="handleLogout">
        <FaIcon icon="sign-out-alt" />
      </NavbarItem>

      <NavbarTogglerControlSidebar title="Toggle Control Sidebar" />
    </NavbarItemGroup>
  </Navbar>
</template>

<script>
import Navbar from '@/components/admin-lte/Navbar'
import NavbarItem from '@/components/admin-lte/NavbarItem'
import NavbarItemGroup from '@/components/admin-lte/NavbarItemGroup'
import NavbarSearch from '@/components/admin-lte/NavbarSearch'
import NavbarTogglerSidebar from '@/components/admin-lte/NavbarTogglerSidebar'
import NavbarTogglerControlSidebar from '@/components/admin-lte/NavbarTogglerControlSidebar'
import { mapActions } from 'vuex'
import { requestCatch } from '@/utils/catchError'

export default {
  name: 'TheNavbar',

  components: {
    Navbar,
    NavbarItem,
    NavbarItemGroup,
    NavbarSearch,
    NavbarTogglerSidebar,
    NavbarTogglerControlSidebar,
  },

  methods: {
    ...mapActions('website/user', [
      'logout',
    ]),

    async handleLogout () {
      try {
        await this.logout()

        this.$router.push({
          name: 'login',
        }, () => {
          this.$notify({
            type: 'success',
            text: 'Logout Successfully.',
          })
        })
      } catch (error) {
        requestCatch(error)
      }
    },
  }
}
</script>
