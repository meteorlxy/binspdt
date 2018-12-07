<template>
  <ErrorPage>
    <span
      slot="code"
      class="text-warning">
      404
    </span>

    <h3>
      <FaIcon
        class="text-warning"
        icon="exclamation-triangle" />

      <span>Oops! Page not found.</span>
    </h3>

    <p>
      We could not find the page you were looking for.
    </p>

    <p>
      Click <RouterLink :to="{ name: 'home' }">here</RouterLink> return to the homepage.
    </p>
  </ErrorPage>
</template>

<script>
import ErrorPage from '@/components/admin-lte/ErrorPage'

export default {
  name: 'NotFound',

  components: {
    ErrorPage,
  },
}
</script>
