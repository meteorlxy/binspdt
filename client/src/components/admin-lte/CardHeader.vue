<template>
  <div class="card-header">
    <slot name="title"/>

    <slot name="tools"/>
  </div>
</template>

<script>
export default {
  name: 'CardHeader',
}
</script>

