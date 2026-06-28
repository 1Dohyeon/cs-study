import { Router, Request, Response } from 'express';
import { prisma } from '../lib/prisma';
import { UserRepository } from '../repositories/user.repository';
import { MeService } from '../services/me.service';
import { authMiddleware } from '../middleware/auth';
import { JwtRequest } from '../types/request';

const userRepository = new UserRepository(prisma);
const meService = new MeService(userRepository);

const router = Router();

// authMiddleware가 먼저 JWT를 검증하고 jwtPayload를 주입한다
// 검증 실패 시 미들웨어에서 401을 응답하고 핸들러는 실행되지 않는다
router.get('/', authMiddleware, async (req: Request, res: Response) => {
  const { userId } = (req as JwtRequest).jwtPayload;
  const user = await meService.getProfile(userId);

  // 유효한 토큰이지만 DB에 유저가 없는 경우 (탈퇴 등)
  if (!user) {
    res.status(404).json({ message: 'User not found' });
    return;
  }

  res.json(user);
});

export default router;
