<template>
  <div class="info-box">
    <span
      class="info-box-icon elevation-1"
      :class="className">
      <slot name="icon">
        <FaIcon
          v-if="icon"
          :icon="icon" />
      </slot>
    </span>

    <div class="info-box-content">
      <span class="info-box-text">
        <slot name="text" />
      </span>

      <span class="info-box-number">
        <slot name="number" />
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BoxInfo',

  props: {
    bg: {
      type: String,
      required: false,
      default: 'info',
    },

    icon: {
      type: [String, Boolean, Array],
      required: false,
      default: false,
    },
  },

  computed: {
    className () {
      return `bg-${this.bg}`
    }
  },
}
</script>
