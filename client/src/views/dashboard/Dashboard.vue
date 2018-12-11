<template>
  <div>
    <TheNavbar @toggle-sidebar="isSidebarOpen = !isSidebarOpen"/>

    <TheSidebar v-model="isSidebarOpen"/>

    <VContent>
      <VLayout
        row
        wrap>
        <VFlex
          xs12
          sm6>
          <h2
            class="pl-3"
            :class="{
              'py-3': $vuetify.breakpoint.mdAndUp,
              'pt-3 pb-0': $vuetify.breakpoint.smAndDown,
            }">
            {{ $route.meta.title }}
          </h2>
        </VFlex>

        <VFlex
          xs12
          sm6
          class="text-sm-right">
          <TheBreadcrumb class="pl-3 d-inline-block"/>
        </VFlex>
      </VLayout>

      <VContainer
        class="px-3 pb-3 pt-0"
        fluid
        full-height>
        <VSlideYReverseTransition mode="out-in">
          <RouterView/>
        </VSlideYReverseTransition>
      </VContainer>
    </VContent>
  </div>
</template>

<script lang="ts">
import TheBreadcrumb from './_components/TheBreadcrumb.vue'
import TheNavbar from './_components/TheNavbar.vue'
import TheSidebar from './_components/TheSidebar.vue'
import { Vue, Component } from 'vue-property-decorator'
import { namespace } from 'vuex-class'

@Component({
  components: {
    TheBreadcrumb,
    TheNavbar,
    TheSidebar,
  },
})
export default class Dashboard extends Vue {
  isSidebarOpen: boolean | null = null

  @namespace('website/user').Action('getUserInfo') getUserInfo
  @namespace('binary/modules').Action('getModules') getModules

  created () {
    this.getUserInfo()
    this.getModules()
  }
}
</script>
