<template>
  <div class="col-12">
    <Card>
      <template slot="title">
        <FaIcon icon="list-ul"/>

        <span class="ml-1">Modules List</span>
      </template>

      <CardBody
        slot="body"
        class="p-0">
        <ATable
          v-if="modules.data.length"
          hover
          striped>
          <thead>
            <tr>
              <th>#</th>

              <th>Name</th>

              <th class="d-none d-sm-table-cell">Architecture</th>

              <th>Upload Time</th>

              <th class="d-none d-md-table-cell">MD5</th>

              <th>Action</th>
            </tr>
          </thead>

          <TransitionFadeSlide
            tag="tbody"
            direction="x"
            group>
            <tr
              v-for="mod in modules.data"
              :key="mod.id">
              <td>{{ mod.id }}</td>

              <td>{{ mod.name }}</td>

              <td class="d-none d-sm-table-cell">{{ mod.architecture }}</td>

              <td>{{ $helpers.formatDateTime(mod.import_time) }}</td>

              <td class="d-none d-md-table-cell">{{ mod.md5 }}</td>

              <td>
                <button
                  class="btn btn-sm btn-primary rounded"
                  title="Inpect Module">
                  <FaIcon :icon="['far', 'eye']" fixed-width/>

                  <span>Inspect</span>
                </button>

                <button
                  class="btn btn-sm btn-danger rounded"
                  title="Delete Module"
                  @click="handleDeleteModule(mod.id)">
                  <FaIcon icon="trash-alt" fixed-width/>

                  <span>Delete</span>
                </button>
              </td>
            </tr>
          </TransitionFadeSlide>
        </ATable>
      </CardBody>

      <CardFooter slot="footer">
      </CardFooter>
    </Card>
  </div>
</template>

<script>
import ATable from '@/components/admin-lte/ATable.vue'
import Card from '@/components/admin-lte/Card.vue'
import CardBody from '@/components/admin-lte/CardBody.vue'
import CardFooter from '@/components/admin-lte/CardFooter.vue'
import TransitionFadeSlide from '@/components/TransitionFadeSlide.vue'
import {
  mapActions,
  mapState,
} from 'vuex'

export default {
  name: 'DashboardModulesList',

  components: {
    ATable,
    Card,
    CardBody,
    CardFooter,
    TransitionFadeSlide,
  },

  computed: {
    ...mapState('binary/modules', [
      'modules',
      'isLoading',
    ]),
  },

  methods: {
    ...mapActions('binary/modules', [
      'deleteModule',
      'postModules',
    ]),

    async handleDeleteModule (id) {
      try {
        await this.deleteModule({ id })
      } catch (e) {

      } finally {

      }
    }
  }
}
</script>
