import jwt from 'jsonwebtoken';
import { UserRepository } from '../repositories/user.repository';

interface GoogleProfile {
  googleId: string;
  email: string;
  name: string;
}

export class AuthService {
  constructor(private readonly userRepository: UserRepository) {}

  async loginWithGoogle(profile: GoogleProfile) {
    // 신규 유저면 insert, 기존 유저면 최신 정보로 update
    const user = await this.userRepository.upsert(profile);

    // expiresIn에 number를 넘기면 초 단위로 인식한다 (15 * 60 = 900초 = 15분)
    // 문자열 '15m'은 TypeScript 타입(StringValue)과 호환되지 않아 number로 전달한다
    const token = jwt.sign(
      { userId: user.id },
      process.env.JWT_SECRET!,
      { expiresIn: Number(process.env.JWT_EXPIRE_MINUTES) * 60 },
    );

    return { user, token };
  }
}
