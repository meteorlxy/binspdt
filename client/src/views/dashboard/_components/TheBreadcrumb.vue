<template>
  <Breadcrumb class="text-muted">
    <BreadcrumbItem>
      <FaIcon
        class="mr-1"
        icon="tachometer-alt"
      />
    </BreadcrumbItem>

    <BreadcrumbItem
      v-for="(route, index) in routeList"
      :key="route.path"
      :to="index === routeList.length - 1 ? '' : route.path">
      {{ route.meta.linkText }}
    </BreadcrumbItem>
  </Breadcrumb>
</template>

<script>
import Breadcrumb from '@/components/admin-lte/Breadcrumb'
import BreadcrumbItem from '@/components/admin-lte/BreadcrumbItem'

export default {
  name: 'TheBreadCrumb',

  components: {
    Breadcrumb,
    BreadcrumbItem,
  },

  computed: {
    routeList () {
      return this.$route.matched.filter(route => route.meta.linkText)
    }
  },
}
</script>
