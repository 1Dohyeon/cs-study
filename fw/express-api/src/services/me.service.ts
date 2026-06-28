import { UserRepository } from '../repositories/user.repository';

export class MeService {
  constructor(private readonly userRepository: UserRepository) {}

  // JWT에서 추출한 userId로 DB에서 프로필을 조회한다
  // 탈퇴하거나 DB에서 삭제된 유저면 null을 반환한다
  async getProfile(userId: number) {
    return this.userRepository.findById(userId);
  }
}
