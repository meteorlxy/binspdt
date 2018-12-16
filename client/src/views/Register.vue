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
                Register a new account for BinSPDT
              </VToolbarTitle>

              <VSpacer/>
            </VToolbar>

            <VCardText>
              <VForm>
                <VTextField
                  v-model="registerForm.username"
                  v-validate="{ required: true, min: 3, max: 30 }"
                  type="text"
                  name="username"
                  label="Username"
                  prepend-icon="person"
                  :error-messages="errors.collect('username')"/>

                <VTextField
                  v-model="registerForm.email"
                  v-validate="{ required: true, email: true, max: 128 }"
                  type="email"
                  name="email"
                  label="Email"
                  prepend-icon="mail"
                  :error-messages="errors.collect('email')"/>

                <VTextField
                  v-model="registerForm.password"
                  v-validate="{ required: true, min: 8, max: 30 }"
                  :type="showPassword ? 'text' : 'password'"
                  name="password"
                  label="Password"
                  prepend-icon="lock"
                  :append-icon="showPassword ? 'visibility_off' : 'visibility'"
                  :error-messages="errors.collect('password')"
                  @click:append="showPassword = !showPassword"/>

                <VTextField
                  v-model="registerForm.passwordConfirm"
                  v-validate="{ required: true, confirmed: 'password' }"
                  :type="showPasswordConfirm ? 'text' : 'password'"
                  name="passwordConfirm"
                  label="Retype Password"
                  prepend-icon="lock_outline"
                  :append-icon="showPasswordConfirm ? 'visibility_off' : 'visibility'"
                  :error-messages="errors.collect('passwordConfirm')"
                  @click:append="showPasswordConfirm = !showPasswordConfirm"/>
              </VForm>
            </VCardText>

            <VCardActions>
              <VBtn
                :to="{ name: 'login' }"
                flat
                small>
                <VIcon
                  class="mr-1"
                  left
                  small>
                  how_to_reg
                </VIcon>

                <span>Already have an account</span>
              </VBtn>

              <VSpacer/>

              <VBtn
                color="primary"
                :disabled="isLoading"
                :loading="isLoading"
                @click="handleRegister">
                <span>Register</span>
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
  registerForm = {
    username: '',
    email: '',
    password: '',
    passwordConfirm: '',
  }

  showPassword: boolean = false
  showPasswordConfirm: boolean = false

  isLoading: boolean = false

  get isFormValid () {
    return !this.errors.any()
  }

  @namespace('website/user').Action('register') register

  async handleRegister (this: any) {
    await this.$validator.validateAll()

    if (!this.isFormValid) {
      return false
    }

    try {
      this.isLoading = true
      const response = await this.register(this.registerForm)

      this.$router.push({
        name: 'login',
      }, () => {
        this.$notify({
          type: 'success',
          text: 'Congratulations! You have already registered a new account. Now you can use it to login BinSPDT.',
        })
      })
    } catch (error) {
      requestCatch(error, (res) => {
        if (res.status === 422 && res.data.errors.hasOwnProperty('username')) {
          this.$notify({
            ...error.notify,
            text: 'Username has already been token!',
          })
          this.errors.add({
            field: 'username',
            msg: 'Username has already been token!',
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
