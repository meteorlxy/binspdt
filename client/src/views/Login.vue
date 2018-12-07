<template>
  <LoginWrapper>
    <LoginLogo>
      <router-link :to="{ name: 'home' }">
        <b>Bin</b>SPDT
      </router-link>
    </LoginLogo>

    <LoginCard>
      <span slot="message">Sign in to BinSPDT</span>

      <LoginInput
        icon="user"
        type="text" 
        name="username"
        placeholder="Username"
        :is-valid="!Boolean(errors.first('username')) && fields['username'] && fields['username'].validated && fields['username'].valid"
        :is-invalid="Boolean(errors.first('username'))"
        :feedback-invalid="errors.first('username')"
        v-validate="{ required: true, min: 3, max: 30 }"
        v-model="loginForm.username">
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
        v-model="loginForm.password">
      </LoginInput>

      <div class="row">
        <div class="col-8">
          <div class="form-check">
            <label class="form-check-label">
              <input
                class="form-check-input"
                type="checkbox"
                v-model="rememberMe">
                <!-- @input="setRememberMe($event.target.value)"> -->
              <span>
                Remember me
              </span>
            </label>
          </div>
        </div>

        <div class="col-4">
          <button
            class="btn btn-primary btn-block btn-flat"
            :disabled="!isFormValid || isLoading"
            @click="handleLogin">
            <FaIcon
              v-show="isLoading"
              class="mr-2"
              icon="spinner"
              spin />
            Sign In
          </button>
        </div>
      </div>

      <p class="text-center my-2">- OR -</p>

      <router-link
        :to="{ name: 'register' }"
        class="d-block mb-1">
        I forgot my password
      </router-link>

      <router-link
        :to="{ name: 'register' }"
        class="d-block">
        Register a new account
      </router-link>
    </LoginCard>
  </LoginWrapper>
</template>

<script>
import LoginCard from '@/components/admin-lte/LoginCard'
import LoginInput from '@/components/admin-lte/LoginInput'
import LoginLogo from '@/components/admin-lte/LoginLogo'
import LoginWrapper from '@/components/admin-lte/LoginWrapper'
import {
  mapActions,
  mapMutations,
} from 'vuex'
import { requestCatch } from '@/utils/catchError'

export default {
  name: 'Login',

  components: {
    LoginCard,
    LoginInput,
    LoginLogo,
    LoginWrapper,
  },

  data () {
    return {
      loginForm: {
        username: '',
        password: '',
      },
      isLoading: false,
    }
  },

  computed: {
    rememberMe: {
      get () {
        return this.$store.state.website.user.rememberMe
      },
      set (val) {
        this.setRememberMe(val)
      }
    },

    isFormValid () {
      return !this.errors.any()
    },
  },

  methods: {
    ...mapActions('website/user', [
      'login',
    ]),

    ...mapMutations('website/user', [
      'setRememberMe',
    ]),

    async handleLogin () {
      await this.$validator.validateAll()

      if (!this.isFormValid) {
        return false
      }

      try {
        this.isLoading = true
        const response = await this.login(this.loginForm)

        if (response.status === 200) {
          this.$router.push({
            path: this.$route.query.redirect || '/',
          }, () => {
            this.$notify({
              type: 'success',
              text: 'Login Successfully.',
            })
          })
        }
      } catch (error) {
        requestCatch(error, (res) => {
          if (res.status === 401) {
            this.$notify({
              type: 'danger',
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
  },
}
</script>

<style lang="scss">
body {
  background: #e9ecef;
}
</style>

