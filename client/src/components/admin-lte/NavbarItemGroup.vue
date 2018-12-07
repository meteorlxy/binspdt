<template>
  <ul
    class="navbar-nav"
    :class="className">
    <slot />
  </ul>
</template>

<script>
export default {
  name: 'NavbarItemGroup',

  props: {
    position: {
      type: String,
      required: false,
      default: 'left',
    },
  },

  computed: {
    className () {
      return this.position === 'right' ? 'ml-auto' : ''
    }
  }
}
</script>

