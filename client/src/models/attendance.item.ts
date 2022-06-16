import {UserItem} from 'src/models/user.item';

export interface AttendanceItem{
  applications: ApplicationItem[];
}

interface ApplicationItem {
  student: UserItem[];
  attendance_start_at: number;
  attendance_end_at: number;
}
