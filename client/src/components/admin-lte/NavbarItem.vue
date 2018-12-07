<template>
  <li class="nav-item">
    <RouterLink
      :is="component"
      class="nav-link"
      :to="to"
      :exact="exact"
    >
      <slot />
    </RouterLink>
  </li>
</template>

<script>
export default {
  name: 'NavbarItem',

  props: {
    to: {
      type: [Object, String],
      required: false,
      default: '',
    },

    exact: {
      type: Boolean,
      required: false,
      default: true,
    },
  },

  computed: {
    component() {
      return this.to === '' ? 'a' : 'RouterLink'
    },
  },
}
</script>
