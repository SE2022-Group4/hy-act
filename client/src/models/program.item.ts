import {UserItem} from "src/models/user.item";

export interface ProgramItem {
  id: number;
  name: string;
  category: number;
  lecturer: UserItem;
  description: string;
  apply_start_at: number;
  apply_end_at: number;
  program_start_at: number;
  program_end_at: number;
  thumbnail_url: string;
  target_grade: string;
  location: string;
  recent_applicant_count: number;
  max_applicant_count: number;
  sex: number;
}
