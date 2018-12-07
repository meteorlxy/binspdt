<template>
  <li class="nav-item">
    <component
      :is="component"
      class="nav-link"
      :to="to"
      :exact="exact"
    >
      <FaIcon
        v-if="icon"
        class="nav-icon"
        :icon="icon" />

      <p>
        <slot />
      </p>
    </component>
  </li>
</template>

<script>
export default {
  name: 'SidebarItem',

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

    icon: {
      type: [String, Boolean, Array],
      required: false,
      default: false,
    },
  },

  computed: {
    component() {
      return this.to === '' ? 'a' : 'RouterLink'
    },
  },
}
</script>
