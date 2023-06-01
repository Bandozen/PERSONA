<template>
  <div>
  <h1>Detail</h1>
  <h3>글제목</h3>
  <p>글 번호 : {{ community?.id }}</p>
  <button @click="communityDelete(community.id)" v-if="isCurrentUser(community?.user)">삭제</button>
  <template v-if="editing">
      <!-- 수정 폼 -->
      <form @submit.prevent="updateCommunity">
        <label for="community-title">제목:</label>
        <input type="text" id="community-title" v-model="updateTitle">
        <label for="community-content">내용:</label>
        <textarea id="community-content" v-model="updateContent"></textarea>
        <button type="submit">수정 완료</button>
      </form>
    </template>

  <template v-else>
    <p>제목: {{ community?.title }}</p>
    <p>내용: {{ community?.content }}</p>
    <p>작성시간: {{ community?.created_at }}</p>
    <p>수정시간: {{ community?.updated_at }}</p>
    <br>
    <p>좋아요개수: {{ community?.community_user_like.length }}</p>
    <button @click="likeCommunity(community.id)">Like</button>
    <br>
    <button @click="editing = true" v-if="isCurrentUser(community?.user)">수정</button>
  </template>

  <div v-for="comment in comments" :key="comment.id">
    <p>내용: {{ comment.content }}</p>
    <p>작성자: {{ comment.user.username }}</p>
    <button @click="commentDelete(comment.id)" v-if="isCurrentUser(comment.user.id)">삭제</button>

    <template v-if="editingCommentId === comment.id">
        <!-- 댓글 수정 폼 -->
        <form @submit.prevent="updateComment(comment.id)">
          <label for="comment-content">수정 내용:</label>
          <input type="text" id="comment-content" v-model="updateCommentContent[comment.id]">
          <button type="submit">수정 완료</button>
        </form>
      </template>
      <template v-else>
        <button @click="editComment(comment.id)" v-if="isCurrentUser(comment.user.id)">수정</button>
      </template>
  </div>

  <form @submit.prevent="createComment">
  <label for="comment-content">댓글 작성:</label>
  <input type="text" id="comment-content" v-model="newCommentContent">
  <button type="submit">등록</button>
</form>

</div>

</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
name: "CommunityDetailView",
data() {
  return {
    community : null,
    comments: null,
    newCommentContent: null,
    editing: false, // 수정 모드 여부
    updateTitle: null,
    updateContent: null,
    editingCommentId: null, // 수정 중인 댓글의 ID
    updateCommentContent: {}, // 수정할 댓글 내용
  }
},
created() {
  this.getCommunityDetail()
},
computed: {
  ...mapState(['token']),
  ...mapState(['user_info'])
},
methods: {
  isCurrentUser(userId) {
    console.log(userId)
    console.log(this.user_info[0].user_id)
    return userId === this.user_info[0].user_id;
  },
  getCommunityDetail() {
    const token = this.token
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/community/${ this.$route.params.id }/`,
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    .then((res) => {
      // console.log(res.data)
      this.community = res.data.community
      this.comments = res.data.comments
    })
    .catch(err => {
      console.log(err)
    })
  },

  createComment() {
    const token = this.token;
    const commentContent = this.newCommentContent;
    const communityId = this.community.id;
    const user_id = this.user_info[0].user_id

    console.log(user_id)
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/community/${communityId}/`,
      data: { content: commentContent, user:user_id},
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        const newComment = res.data;
        this.comments.push(newComment);
        this.newCommentContent = ''; // 댓글 작성 폼 초기화
        console.log('댓글이 성공적으로 생성되었습니다:', newComment);
      })
      .catch((err) => {
        console.log('댓글 생성에 실패했습니다:', err);
      });
  },
  commentDelete(commentId) {
    // console.log(commentId)
    const token = this.token;
    const communityId = this.community.id
    if (!this.isCurrentUser(this.comments.find(comment => comment.id === commentId).user.id)) {
    console.log("해당 댓글을 삭제할 권한이 없습니다.");
    return;
  }
    axios({
      method: 'delete',
      url: `${API_URL}/api/v1/community/${communityId}/comments/${commentId}/`,
      data: {community_pk: communityId, comment_pk: commentId},
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
      .then(() => {
        // console.log('삭제완료.')
        // console.log(res)
        this.comments = this.comments.filter(comment => comment.id !== commentId);
      })
      .catch(err => {
        console.log(err)
      })
  },
  editComment(commentId) {
    this.editingCommentId = commentId;
    this.$set(this.updateCommentContent[commentId] = this.comments.find(comment => comment.id === commentId).content);
  },

  updateComment(commentId) {
  const token = this.token;
  const communityId = this.community.id;
  const updatedContent = this.updateCommentContent[commentId];
  const community = this.community
  const user_id = this.user_info[0].user_id
    axios({
      method: 'put', 
      url: `${API_URL}/api/v1/community/${communityId}/comments/${commentId}/`,
      data: { content: updatedContent, community: community,
      user: user_id },
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then(() => {
        console.log(111)
        this.editingCommentId = null; // 수정 모드 종료
        const updatedCommentIndex = this.comments.findIndex(comment => comment.id === commentId);
        this.comments[updatedCommentIndex].content = updatedContent;
      })
      .catch(err => {
        console.log(err);
      });
  },

  updateCommunity() {
    const token = this.token
    const communityId = this.community.id
    const updatedTitle = this.updateTitle
    const updatedContent = this.updateContent
    const user_id = this.user_info[0].user_id
    this.community.title = updatedTitle
    this.community.content = updatedContent
    if (!this.isCurrentUser(this.community.user)) {

      console.log('해당 글을 수정할 권한이 없습니다.')
      return
    }
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/community/${communityId}/`,
        data: {
          content: updatedContent,
          title: updatedTitle,
          community_user_like: [], // 고쳐야됨
          user:user_id
        },
        headers: {
          Authorization: `Bearer ${token}`,
        },
      })
        .then(() => {
          this.editing = false; // 수정 모드 종료
          this.community.title = updatedTitle; // 제목 업데이트
          this.community.content = updatedContent;
        })
        .catch(err=> {
          console.log(this.community)
          console.log(err)
        })
  },
  communityDelete(communityId) {
    console.log(communityId)
    const token = this.token;
    if (!this.isCurrentUser(this.community.user)) {
    console.log("해당 글을 삭제할 권한이 없습니다.");
    return;
  }
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/${communityId}/`,
        data: {community_pk: communityId},
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then(() => {
          console.log('삭제완료.')
          this.$router.push('/community')
        })
        .catch(err => {
          console.log(err)
        })
  },
  likeCommunity(communityId) {
  const token = this.token;
  const userId = this.user_info[0].user_id;
  axios({
    method: 'post',
    url: `${API_URL}/api/v1/community/${communityId}/likes/`,
    data: {
      userId
    },
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })
    .then(() => {
      console.log('커뮤니티 좋아요가 성공적으로 등록되었습니다.');
      // 로컬에서 community_user_like 리스트 업데이트
      this.fetchCommunityLikes(communityId)
    })
    .catch(err => {
      console.log(err);
    });
  },
  fetchCommunityLikes(communityId){
    const token = this.token
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/community/${communityId}/`,
      data: {
        community_pk: communityId
      },
      headers: {
      Authorization: `Bearer ${token}`,
    },
    })
      .then((res) => {
        //서버에서 받아온 좋아요 개수 업데이트
        this.community = res.data.community
      })
      .catch(err => {
        console.log(err)
      })
  }
}
}
</script>

<style>

</style>