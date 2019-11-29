import session from "./session";

export default {
  login(username, password) {
    return session.post(
      `${process.env.VUE_APP_BACK_BASE_URL}/rest-auth/login/`,
      { username, password }
    );
  },
  logout() {
    return session.post(
      `${process.env.VUE_APP_BACK_BASE_URL}/rest-auth/logout/`,
      {}
    );
  },
  createAccount(username, password1, password2, email) {
    return session.post(
      `${process.env.VUE_APP_BACK_BASE_URL}/rest-auth/signup/`,
      {
        username,
        password1,
        password2,
        email
      }
    );
  },
  changeAccountPassword({ oldPassword, newPassword1, newPassword2 }) {
    return session.post(
      `${process.env.VUE_APP_BACK_BASE_URL}/rest-auth/password/change/`,
      {
        old_password: oldPassword,
        new_password1: newPassword1,
        new_password2: newPassword2
      }
    );
  },
  sendAccountPasswordResetEmail(email) {
    return session.post(
      `${process.env.VUE_APP_BACK_BASE_URL}/rest-auth/password/reset/`,
      { email }
    );
  },
  resetAccountPassword(uid, token, new_password1, new_password2) {
    // eslint-disable-line camelcase
    return session.post(
      `${process.env.VUE_APP_BACK_BASE_URL}/rest-auth/password/reset/confirm/`,
      {
        uid,
        token,
        new_password1,
        new_password2
      }
    );
  },
  getAccountDetails() {
    return session.get(`${process.env.VUE_APP_BACK_BASE_URL}/rest-auth/user/`);
  },
  updateAccountDetails(data) {
    return session.patch(
      `${process.env.VUE_APP_BACK_BASE_URL}/rest-auth/user/`,
      data
    );
  },
  verifyAccountEmail(key) {
    return session.post("/registration/verify-email/", { key });
  }
};
