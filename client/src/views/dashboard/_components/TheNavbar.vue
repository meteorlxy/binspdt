<template>
  <VToolbar
    app
    clipped-left
    dark>
    <VToolbarSideIcon @click.stop="$emit('toggle-sidebar')"/>

    <VToolbarTitle>
      BinSPDT
    </VToolbarTitle>

    <VSpacer/>

    <VBtn
      icon
      @click="handleLogout">
      <VIcon>logout</VIcon>
    </VBtn>
  </VToolbar>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
import { namespace } from 'vuex-class'
import { requestCatch } from '@/utils/catchError'

@Component
export default class TheNavbar extends Vue {
  drawer: any = null

  @namespace('website/user').Action('logout') logout

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
  }
}
</script>
