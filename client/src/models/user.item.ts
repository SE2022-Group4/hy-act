export interface UserItem {
  username: string;
  email: string;
  firstname: string;
  lastname: string;
  groups: UserGroup[];
  telephone: string;
  departments: string[];
}

interface UserGroup {
  name: string;
}
