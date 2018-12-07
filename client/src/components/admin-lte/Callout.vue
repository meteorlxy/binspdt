<template>
  <div
    class="callout"
    :class="className">
    <h5>
      <slot name="title" />
    </h5>
    
    <p>
      <slot name="text" />
    </p>
  </div>
</template>

<script>
export default {
  name: 'Callout',

  props: {
    type: {
      type: String,
      required: false,
      default: 'info',
      validator: value => ['info', 'success', 'warning', 'danger'].includes(value),
    },
  },

  computed: {
    className () {
      return [
        `callout-${this.type}`,
      ]
    },
  },
}
</script>
