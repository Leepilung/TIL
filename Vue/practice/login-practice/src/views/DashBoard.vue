<template>
  <div>
    <h1>Dashboard</h1>
    <template v-if="!isLoading">
      <EventCard v-for="event in events" :key="event.id" :event="event" />
    </template>
    <p v-else>Loading events</p>
  </div>
</template>

<script>
import axios from 'axios'
import EventCard from '../components/EventCard.vue'

export default {
  components: { EventCard },
  data() {
    return {
      isLoading: true,
      events: [],
      token: localStorage.getItem('token'),
    }
  },
  created() {
    // data에서 가져올때 string 형태이기 때문에 json으로 파싱 다시해줘야함.
    if (this.token) {
      console.log('토큰 : ', JSON.parse(this.token).token)
      this.token = JSON.parse(this.token).token
      // this.$store.commit('SET_USER_DATA', this.token);
      axios.defaults.headers.common.Authorization = `Bearer ${this.token}`
    }
    console.log(this.token)
    if (this.token !== null) {
      console.log('엑시오스 실행')
      axios
        .get('//localhost:3000/dashboard')
        .then(({ data }) => {
          console.log('통신 성공')
          this.events = data.events.events
          this.isLoading = false
        })
        .catch(err => {
          console.log('에러 발생 :', err)
        })
    }
  },
}
</script>
