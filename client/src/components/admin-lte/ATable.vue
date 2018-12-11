<template>
  <table
    class="table"
    :class="tableClass">
    <slot/>
  </table>
</template>

<script>
export default {
  name: 'ATable',

  props: {
    bordered: {
      type: Boolean,
      required: false,
      default: false,
    },

    borderless: {
      type: Boolean,
      required: false,
      default: false,
    },

    dark: {
      type: Boolean,
      required: false,
      default: false,
    },

    hover: {
      type: Boolean,
      required: false,
      default: false,
    },

    responsive: {
      type: Boolean,
      required: false,
      default: false,
    },

    responsiveSm: {
      type: Boolean,
      required: false,
      default: false,
    },

    responsiveMd: {
      type: Boolean,
      required: false,
      default: false,
    },

    responsiveLg: {
      type: Boolean,
      required: false,
      default: false,
    },

    responsiveXl: {
      type: Boolean,
      required: false,
      default: false,
    },

    striped: {
      type: Boolean,
      required: false,
      default: false,
    },
  },

  computed: {
    tableClass () {
      return {
        'table-bordered': this.bordered,
        'table-borderless': this.borderless,
        'table-dark': this.dark,
        'table-hover': this.hover,
        'table-responsive': this.responsive,
        'table-responsive-sm': this.responsiveSm,
        'table-responsive-md': this.responsiveMd,
        'table-responsive-lg': this.responsiveLg,
        'table-responsive-xl': this.responsiveXl,
        'table-striped': this.striped,
      }
    },
  },
}
</script>

