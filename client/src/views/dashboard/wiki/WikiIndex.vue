<template>
  <VCard>
    <VCardText>
      <VSubheader>Index of Wiki</VSubheader>

      <ul>
        <li>
          <RouterLink :to="{ name: 'dashboard.wiki.api-set' }">
            API Set - Set of System API Calls in Functions
          </RouterLink>
        </li>
      </ul>
    </VCardText>
  </VCard>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component
export default class WikiIndex extends Vue {
}
</script>
