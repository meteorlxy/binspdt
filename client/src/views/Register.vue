<template>
  <LoginWrapper>
    <LoginLogo>
      <RouterLink :to="{ name: 'home' }">
        <b>Bin</b>SPDT
      </RouterLink>
    </LoginLogo>

    <LoginCard>
      <span slot="message">Register a new account for BinSPDT</span>

      <LoginInput
        icon="user"
        type="text" 
        name="username"
        placeholder="Username"
        :is-valid="!Boolean(errors.first('username')) && fields['username'] && fields['username'].validated && fields['username'].valid"
        :is-invalid="Boolean(errors.first('username'))"
        :feedback-invalid="errors.first('username')"
        v-validate="{ required: true, min: 3, max: 30 }"
        v-model="registerForm.username">
      </LoginInput>

      <LoginInput
        icon="envelope"
        type="email" 
        name="email"
        placeholder="Email"
        :is-valid="!Boolean(errors.first('email')) && fields['email'] && fields['email'].validated && fields['email'].valid"
        :is-invalid="Boolean(errors.first('email'))"
        :feedback-invalid="errors.first('email')"
        v-validate="{ required: true, email: true, max: 128 }"
        v-model="registerForm.email">
      </LoginInput>

      <LoginInput
        icon="lock"
        type="password" 
        name="password"
        ref="password"
        placeholder="Password"
        :is-valid="!Boolean(errors.first('password')) && fields['password'] && fields['password'].validated && fields['password'].valid"
        :is-invalid="Boolean(errors.first('password'))"
        :feedback-invalid="errors.first('password')"
        v-validate="{ required: true, min: 8, max: 30 }"
        v-model="registerForm.password">
      </LoginInput>

      <LoginInput
        icon="user-lock"
        type="password" 
        name="passwordConfirm"
        placeholder="Retype Password"
        data-vv-as="retype password"
        :is-valid="!Boolean(errors.first('passwordConfirm')) && fields['passwordConfirm'] && fields['passwordConfirm'].validated && fields['passwordConfirm'].valid"
        :is-invalid="Boolean(errors.first('passwordConfirm'))"
        :feedback-invalid="errors.first('passwordConfirm')"
        v-validate="{ required: true, confirmed: 'password' }"
        v-model="registerForm.passwordConfirm">
      </LoginInput>

      <button
        class="btn btn-primary btn-block btn-flat"
        :disabled="!isFormValid || isLoading"
        @click="handleRegister">
        <FaIcon
          v-show="isLoading"
          class="mr-2"
          icon="spinner"
          spin />

        <span>Register</span>
      </button>

      <p class="text-center my-2">- OR -</p>

      <RouterLink
        :to="{ name: 'login' }"
        class="d-block">
        I already have an account
      </RouterLink>
    </LoginCard>
  </LoginWrapper>
</template>

<script>
import LoginCard from '@/components/admin-lte/LoginCard'
import LoginInput from '@/components/admin-lte/LoginInput'
import LoginLogo from '@/components/admin-lte/LoginLogo'
import LoginWrapper from '@/components/admin-lte/LoginWrapper'
import { mapActions } from 'vuex'
import { requestCatch } from '@/utils/catchError'

export default {
  name: 'Register',

  components: {
    LoginCard,
    LoginInput,
    LoginLogo,
    LoginWrapper,
  },

  data () {
    return {
      registerForm: {
        username: '',
        email: '',
        password: '',
        passwordConfirm: '',
      },
      isLoading: false,
    }
  },

  computed: {
    isFormValid () {
      return !this.errors.any()
    },
  },

  methods: {
    ...mapActions('website/user', [
      'register',
    ]),

    async handleRegister () {
      await this.$validator.validateAll()

      if (!this.isFormValid) {
        return false
      }

      try {
        this.isLoading = true
        const response = await this.register(this.registerForm)

        if (response.status === 201) {
          this.$router.push({
            name: 'login',
          }, () => {
            this.$notify({
              type: 'success',
              text: 'Congratulations! You have already registered a new account. Now you can use it to login BinSPDT.',
            })
          })
        } else {
          throw new Error(`${response.status} ${response.statusText}: ${response.data.message}`)
        }
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
    },
  },
}
</script>

<style lang="scss">
body {
  background: #e9ecef;
}
</style>

