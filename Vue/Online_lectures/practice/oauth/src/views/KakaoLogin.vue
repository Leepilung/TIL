<template>
  <div>
    <a id="custom-login-btn" @click="kakaoLogin()">
      <img
        src="//k.kakaocdn.net/14/dn/btqCn0WEmI3/nijroPfbpCa4at5EIsjyf0/o.jpg"
        width="222"
      />
    </a>
    <br/>
    <button type="button" @click="kakaoLogout">카카오 로그아웃</button>
  </div>
</template>
<script>
// import axios from 'axios'
export default {
  components: {},
  data () {
    return {
      code: ''
    }
  },
  mounted () {
    // Kakao.init('c2875030d590c5acc4f04aa15597bab4');
    // Kakao.isInitialized();
    // this.kakaoLogout();
  },
  methods: {
    kakaoLogin () {
      // kakao sdk에서 제공하는 메소드
      window.Kakao.Auth.login({
        // scope은 우리가 동의항목에 설정해둔 요소들
        scope: 'profile_nickname, account_email',
        success: this.getKakaoAccount
      })
    },
    getKakaoAccount () {
      window.Kakao.API.request({
        url: '/v2/user/me',
        success: (res) => {
          console.log('결과 :', res)
          const kakaoAccount = res.kakao_account
          const username = kakaoAccount.profile.nickname // 카카오 닉네임
          const email = kakaoAccount.email // 카카오 이메일
          console.log('username :', username)
          console.log('email :', email)

          // 로그인 처리 구현
          console.log(kakaoAccount)
          this.$store.commit('user', kakaoAccount)
          alert('로그인 성공!')
        },
        fail: (error) => {
          // this.$router.push("/errorPage");
          console.log(error)
        }
      })
    },
    kakaoLogout () {
      if (!window.Kakao.Auth.getAccessToken()) {
        console.log('Not logged in.')
        return
      }
      window.Kakao.Auth.logout((response) => {
        // 로그아웃
        console.log('access token:', window.Kakao.Auth.getAccessToken())
        console.log('log out:', response)
      })
    }
  }
}
</script>
