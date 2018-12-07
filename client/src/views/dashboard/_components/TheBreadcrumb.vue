<template>
  <Breadcrumb>
    <BreadcrumbItem
      v-for="(route, index) in $route.matched"
      :key="route.path"
      :to="index === $route.matched.length - 1 ? '' : route.path">
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
}
</script>
