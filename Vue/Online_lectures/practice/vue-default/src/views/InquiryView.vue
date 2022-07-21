<template lang="">
	<div>
		<div>
			<select v-model="selectedCity">
				<option :value="city.code" :key="i" v-for="(city, i) in cityList">
					{{ city.name }}
				</option>
			</select>
			<input type="text" v-model="userName" @keyup.enter="searchUserList" />
			<button type="button" @click="searchUserList">조회</button>
		</div>
		<div>
			<table>
				<thead>
					<tr>
						<th>이름</th>
						<th>나이</th>
						<th>직업</th>
					</tr>
				</thead>
				<tbody>
					<tr :key="i" v-for="(person, i) in userList">
						<td>{{ person.name }}</td>
						<td>{{ person.age }}</td>
						<td>{{ person.job }}</td>
					</tr>
				</tbody>
			</table>
		</div>
	</div>
</template>
<script>
export default {
	data() {
		return {
			cityList: [
				{ name: '서울', code: '02' },
				{ name: '경기도', code: '031' },
				{ name: '강원도', code: '032' },
			],
			selectedCity: '',
			userName: '',
			userList: [],
		};
	},
	methods: {
		searchUserList() {
			const params = {
				selectedCity: this.selectedCity,
				userName: this.userName,
			};

			this.userList = this.getUserList(params);
			console.log(this.userList);
		},
		getUserList(params) {
			console.log(params);

			let list = [
				{ name: '유재석', age: 50, job: '연애인' },
				{ name: '하하', age: 35, job: '연애인' },
				{ name: '김종국', age: 47, job: '연애인' },
				{ name: '양세찬', age: 30, job: '연애인' },
			];

			return list;
		},
	},
};
</script>
<style lang=""></style>
