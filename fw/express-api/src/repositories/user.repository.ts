import { PrismaClient } from '@prisma/client';

// DB 접근만 담당한다. 비즈니스 로직은 Service에서 처리한다
export class UserRepository {
  constructor(private readonly prisma: PrismaClient) {}

  async findById(id: number) {
    return this.prisma.user.findUnique({ where: { id } });
  }

  async upsert(data: { googleId: string; email: string; name: string }) {
    // googleId 기준으로 이미 존재하면 email·name을 갱신하고, 없으면 새로 생성한다
    // Google 계정의 이름·이메일이 변경됐을 때 자동으로 동기화된다
    return this.prisma.user.upsert({
      where: { googleId: data.googleId },
      update: { email: data.email, name: data.name },
      create: data,
    });
  }
}
