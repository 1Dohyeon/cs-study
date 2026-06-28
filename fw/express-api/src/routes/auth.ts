import { Router, Request, Response } from 'express';
import passport from 'passport';
import { Strategy as GoogleStrategy } from 'passport-google-oauth20';
import { prisma } from '../lib/prisma';
import { UserRepository } from '../repositories/user.repository';
import { AuthService } from '../services/auth.service';
import { GoogleCallbackRequest } from '../types/request';

// 의존성을 직접 연결한다 (NestJS의 DI 컨테이너 역할을 수동으로 수행)
const userRepository = new UserRepository(prisma);
const authService = new AuthService(userRepository);

// Google OAuth 전략을 passport에 등록한다
// 이 코드는 모듈 로드 시 한 번만 실행된다
passport.use(
  new GoogleStrategy(
    {
      clientID: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
      callbackURL: process.env.GOOGLE_CALLBACK_URL!,
    },
    async (_accessToken, _refreshToken, profile, done) => {
      try {
        // Google에서 받은 프로필로 DB upsert 후 JWT를 발급한다
        // done(null, result)로 넘긴 값이 req.user에 담긴다
        const result = await authService.loginWithGoogle({
          googleId: profile.id,
          email: profile.emails![0].value,
          name: profile.displayName,
        });
        done(null, result as never);
      } catch (e) {
        done(e as Error);
      }
    },
  ),
);

const router = Router();

// Google 로그인 페이지로 리다이렉트한다
// scope: profile(이름)과 email 정보를 요청한다
router.get('/google', passport.authenticate('google', { scope: ['profile', 'email'] }));

router.get(
  '/google/callback',
  // session: false → 세션 없이 JWT만으로 인증 상태를 관리한다
  passport.authenticate('google', { session: false }),
  (req: Request, res: Response) => {
    // passport가 전략 콜백에서 done(null, result)로 넘긴 값이 req.user에 담겨 있다
    const { token } = (req as GoogleCallbackRequest).user;
    res.redirect(`/callback?token=${token}`);
  },
);

export default router;
