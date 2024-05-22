/* eslint-disable */

import uploadPhoto from "./utils";
import CreateUser from "./utils";

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), CreateUser()])
    .then((values) => {
      const [photo, user] = values;
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => console.log("Signup system offline"));
}
