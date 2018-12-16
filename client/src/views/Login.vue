<template>
  <VContent>
    <VContainer
      fluid
      fill-height>
      <VLayout
        align-center
        justify-center>
        <VFlex
          xs12
          sm8
          md6
          lg4>
          <VCard class="elevation-12">
            <VToolbar
              flat
              color="white">
              <VToolbarTitle>
                Login to BinSPDT
              </VToolbarTitle>

              <VSpacer/>
            </VToolbar>

            <VCardText>
              <VForm>
                <VTextField
                  v-model="loginForm.username"
                  v-validate="{ required: true, min: 3, max: 30 }"
                  type="text"
                  name="username"
                  label="Username"
                  prepend-icon="person"
                  :error-messages="errors.collect('username')"
                  @keyup.enter="handleLogin"/>

                <VTextField
                  v-model="loginForm.password"
                  v-validate="{ required: true, min: 8, max: 30 }"
                  :type="showPassword ? 'text' : 'password'"
                  name="password"
                  label="Password"
                  prepend-icon="lock"
                  :append-icon="showPassword ? 'visibility_off' : 'visibility'"
                  :error-messages="errors.collect('password')"
                  @click:append="showPassword = !showPassword"
                  @keyup.enter="handleLogin"/>
              </VForm>
            </VCardText>

            <VCardActions>
              <VBtn
                :to="{ name: 'register' }"
                flat
                small>
                <VIcon
                  class="mr-1"
                  left
                  small>
                  person_add
                </VIcon>

                <span>Regiter a new account</span>
              </VBtn>

              <VSpacer/>

              <VBtn
                color="primary"
                :disabled="isLoading || !isFormValid"
                :loading="isLoading"
                @click="handleLogin">
                <span>Login</span>
              </VBtn>
            </VCardActions>
          </VCard>
        </VFlex>
      </VLayout>
    </VContainer>
  </VContent>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { namespace } from 'vuex-class'
import { requestCatch } from '@/utils/catchError'

@Component
export default class Login extends Vue {
  loginForm = {
    username: '',
    password: '',
  }

  showPassword: boolean = false

  isLoading: boolean = false

  get isFormValid () {
    return !this.errors.any()
  }

  @namespace('website/user').Action('login') login

  async handleLogin () {
    await this.$validator.validateAll()

    if (!this.isFormValid) {
      return false
    }

    try {
      this.isLoading = true
      await this.login(this.loginForm)

      this.$router.push({
        path: <string> this.$route.query.redirect || '/',
      }, () => {
        this.$notify({
          type: 'success',
          text: 'Login Successfully.',
        })
      })
    } catch (error) {
      requestCatch(error, (res) => {
        if (res.status === 401) {
          this.$notify({
            type: 'error',
            title: 'Login Failed',
            text: 'Incorrect username or password.',
          })
        } else {
          this.$notify(error.notify)
        }
      })
    } finally {
      this.isLoading = false
    }
  }
}
</script>
