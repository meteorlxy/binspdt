<template>
  <div class="wrapper">
    <TheNavbar />

    <TheSidebar />

    <TheControlSidebar />

    <TheMainContent>
      <RouterView />
    </TheMainContent>

    <TheMainFooter />
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import TheControlSidebar from './_components/TheControlSidebar'
import TheMainContent from './_components/TheMainContent'
import TheMainFooter from './_components/TheMainFooter'
import TheNavbar from './_components/TheNavbar'
import TheSidebar from './_components/TheSidebar'

export default {
  name: 'Dashboard',

  components: {
    TheControlSidebar,
    TheMainContent,
    TheMainFooter,
    TheNavbar,
    TheSidebar,
  },

  created () {
    this.getUserInfo()
    this.getModules()
  },

  mounted () {
    this.$adminlte.init()
  },

  methods: {
    ...mapActions('website/user', [
      'getUserInfo',
    ]),

    ...mapActions('binary/modules', [
      'getModules',
    ]),
  },
}
</script>

<style lang="scss">
.nav-link {
  cursor: pointer;
}
</style>
