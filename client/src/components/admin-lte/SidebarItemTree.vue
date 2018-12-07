<template>
  <li class="nav-item has-treeview">
    <a class="nav-link">
      <FaIcon
        v-if="icon"
        class="nav-icon"
        :icon="icon"/>

      <p>
        <slot name="title" />

        <FaIcon
          class="right"
          icon="angle-left" />
      </p>
    </a>

    <ul class="nav nav-treeview">
      <slot />
    </ul>
  </li>
</template>

<script>
export default {
  name: 'SidebarItemTree',

  props: {
    icon: {
      type: [String, Boolean, Array],
      required: false,
      default: false,
    },
  },
}
</script>

<style lang="scss" scoped>
.nav-link {
  cursor: pointer;
}
</style>

